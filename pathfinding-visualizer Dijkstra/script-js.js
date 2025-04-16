document.addEventListener('DOMContentLoaded', function() {
    // Grid setup
    const gridElement = document.getElementById('grid');
    const startBtn = document.getElementById('start-btn');
    const resetBtn = document.getElementById('reset-btn');
    const speedSlider = document.getElementById('speed');
    const wallModeBtn = document.getElementById('wall-mode');
    const startModeBtn = document.getElementById('start-mode');
    const endModeBtn = document.getElementById('end-mode');
    const currentModeText = document.getElementById('current-mode');

    const ROWS = 20;
    const COLS = 30;
    let grid = [];
    let isMouseDown = false;
    let startCell = null;
    let endCell = null;
    let currentMode = 'wall'; // 'wall', 'start', or 'end'
    let isVisualizationRunning = false;

    // Create the grid
    function createGrid() {
        gridElement.innerHTML = '';
        grid = [];

        for (let row = 0; row < ROWS; row++) {
            const rowArray = [];
            for (let col = 0; col < COLS; col++) {
                const cell = document.createElement('div');
                cell.className = 'cell';
                cell.dataset.row = row;
                cell.dataset.col = col;
                
                cell.addEventListener('mousedown', handleMouseDown);
                cell.addEventListener('mouseenter', handleMouseEnter);
                cell.addEventListener('mouseup', handleMouseUp);
                
                gridElement.appendChild(cell);
                
                rowArray.push({
                    element: cell,
                    isWall: false,
                    isStart: false,
                    isEnd: false,
                    isVisited: false,
                    isPath: false,
                    distance: Infinity,
                    previousCell: null
                });
            }
            grid.push(rowArray);
        }

        // Set default start and end positions
        setStartCell(grid[10][5]);
        setEndCell(grid[10][25]);
    }

    function handleMouseDown(e) {
        isMouseDown = true;
        const row = parseInt(e.target.dataset.row);
        const col = parseInt(e.target.dataset.col);
        
        if (isVisualizationRunning) return;
        
        if (currentMode === 'wall') {
            toggleWall(grid[row][col]);
        } else if (currentMode === 'start') {
            setStartCell(grid[row][col]);
        } else if (currentMode === 'end') {
            setEndCell(grid[row][col]);
        }
    }

    function handleMouseEnter(e) {
        if (isMouseDown && currentMode === 'wall' && !isVisualizationRunning) {
            const row = parseInt(e.target.dataset.row);
            const col = parseInt(e.target.dataset.col);
            toggleWall(grid[row][col]);
        }
    }

    function handleMouseUp() {
        isMouseDown = false;
    }

    function toggleWall(cell) {
        if (cell.isStart || cell.isEnd) return;
        
        cell.isWall = !cell.isWall;
        cell.element.classList.toggle('wall', cell.isWall);
    }

    function setStartCell(cell) {
        if (cell.isWall || cell.isEnd) return;
        
        if (startCell) {
            startCell.isStart = false;
            startCell.element.classList.remove('start');
        }
        
        startCell = cell;
        cell.isStart = true;
        cell.element.classList.add('start');
    }

    function setEndCell(cell) {
        if (cell.isWall || cell.isStart) return;
        
        if (endCell) {
            endCell.isEnd = false;
            endCell.element.classList.remove('end');
        }
        
        endCell = cell;
        cell.isEnd = true;
        cell.element.classList.add('end');
    }

    function resetGrid() {
        isVisualizationRunning = false;
        startBtn.disabled = false;
        
        for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
                const cell = grid[row][col];
                cell.isVisited = false;
                cell.isPath = false;
                cell.distance = Infinity;
                cell.previousCell = null;
                cell.element.classList.remove('visited', 'path');
            }
        }
    }

    function clearEverything() {
        resetGrid();
        for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
                const cell = grid[row][col];
                cell.isWall = false;
                cell.element.classList.remove('wall');
            }
        }
        setStartCell(grid[10][5]);
        setEndCell(grid[10][25]);
    }

    // Dijkstra's algorithm
    async function runDijkstra() {
        if (!startCell || !endCell) return;
        
        isVisualizationRunning = true;
        startBtn.disabled = true;
        resetGrid();
        
        // Initialize distances
        startCell.distance = 0;
        
        const unvisitedNodes = getAllNodes();
        
        while (unvisitedNodes.length > 0) {
            // Sort by distance
            unvisitedNodes.sort((a, b) => a.distance - b.distance);
            
            // Get closest node
            const closestNode = unvisitedNodes.shift();
            
            // If we encounter a wall, skip it
            if (closestNode.isWall) continue;
            
            // If the closest node is at a distance of infinity, we are trapped
            if (closestNode.distance === Infinity) break;
            
            closestNode.isVisited = true;
            if (!closestNode.isStart && !closestNode.isEnd) {
                closestNode.element.classList.add('visited');
                await sleep(200 - speedSlider.value); // Animation speed
            }
            
            // If we found the end, visualize the path
            if (closestNode === endCell) {
                await visualizePath();
                isVisualizationRunning = false;
                startBtn.disabled = false;
                return;
            }
            
            // Update unvisited neighbors
            updateUnvisitedNeighbors(closestNode);
        }
        
        // If we get here, there is no path
        alert('No path found!');
        isVisualizationRunning = false;
        startBtn.disabled = false;
    }

    function getAllNodes() {
        const nodes = [];
        for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
                nodes.push(grid[row][col]);
            }
        }
        return nodes;
    }

    function updateUnvisitedNeighbors(node) {
        const neighbors = getNeighbors(node);
        for (const neighbor of neighbors) {
            neighbor.distance = node.distance + 1;
            neighbor.previousCell = node;
        }
    }

    function getNeighbors(node) {
        const neighbors = [];
        const { row, col } = getNodeIndices(node);
        
        // Check the four directions
        if (row > 0) neighbors.push(grid[row - 1][col]); // Up
        if (row < ROWS - 1) neighbors.push(grid[row + 1][col]); // Down
        if (col > 0) neighbors.push(grid[row][col - 1]); // Left
        if (col < COLS - 1) neighbors.push(grid[row][col + 1]); // Right
        
        // Filter out visited nodes and walls
        return neighbors.filter(neighbor => !neighbor.isVisited && !neighbor.isWall);
    }

    function getNodeIndices(node) {
        for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
                if (grid[row][col] === node) {
                    return { row, col };
                }
            }
        }
        return { row: -1, col: -1 };
    }

    async function visualizePath() {
        let currentNode = endCell;
        const path = [];
        
        while (currentNode !== null && currentNode !== startCell) {
            path.push(currentNode);
            currentNode = currentNode.previousCell;
        }
        
        // Reverse to get start-to-end path
        path.reverse();
        
        // Animate the path
        for (const node of path) {
            node.isPath = true;
            node.element.classList.add('path');
            await sleep(30);
        }
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Event listeners
    startBtn.addEventListener('click', runDijkstra);
    resetBtn.addEventListener('click', clearEverything);
    
    wallModeBtn.addEventListener('click', () => {
        currentMode = 'wall';
        currentModeText.textContent = 'Wall';
    });
    
    startModeBtn.addEventListener('click', () => {
        currentMode = 'start';
        currentModeText.textContent = 'Start Point';
    });
    
    endModeBtn.addEventListener('click', () => {
        currentMode = 'end';
        currentModeText.textContent = 'End Point';
    });

    document.addEventListener('mouseup', () => {
        isMouseDown = false;
    });

    // Initialize the grid
    createGrid();
});
