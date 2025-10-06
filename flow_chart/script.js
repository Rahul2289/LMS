// LMS Flow Diagram Data Structure
const flowData = {
    id: 'start',
    label: 'LMS Welcome Screen',
    type: 'start',
    children: [
        {
            id: 'select-role',
            label: 'Select Your Role',
            type: 'role',
            children: [
                {
                    id: 'admin-login',
                    label: 'Admin Login',
                    type: 'admin',
                    badge: 'ADMIN',
                    children: [
                        {
                            id: 'admin-menu',
                            label: 'Admin Dashboard',
                            type: 'admin',
                            expandable: true,
                            children: [
                                { id: 'add-admin', label: 'Add New Admin', type: 'action' },
                                { id: 'add-student', label: 'Add Student', type: 'action' },
                                { id: 'add-teacher', label: 'Add Teacher', type: 'action' },
                                { id: 'add-book', label: 'Add Books', type: 'action' },
                                { id: 'update-student', label: 'Update Student', type: 'action' },
                                { id: 'update-teacher', label: 'Update Teacher', type: 'action' },
                                { id: 'update-book', label: 'Update Books', type: 'action' },
                                { id: 'delete-student', label: 'Delete Student', type: 'action' },
                                { id: 'delete-teacher', label: 'Delete Teacher', type: 'action' },
                                { id: 'delete-book', label: 'Delete Books', type: 'action' },
                                { id: 'admin-logout', label: 'Logout', type: 'end' }
                            ]
                        }
                    ]
                },
                {
                    id: 'student-login',
                    label: 'Student Login',
                    type: 'student',
                    badge: 'STUDENT',
                    children: [
                        {
                            id: 'student-menu',
                            label: 'Student Dashboard',
                            type: 'student',
                            expandable: true,
                            children: [
                                { id: 'view-books-s', label: 'View Books', type: 'action' },
                                { id: 'take-books-s', label: 'Take Books', type: 'action' },
                                { id: 'return-books-s', label: 'Return Books', type: 'action' },
                                { id: 'student-logout', label: 'Logout', type: 'end' }
                            ]
                        }
                    ]
                },
                {
                    id: 'teacher-login',
                    label: 'Teacher Login',
                    type: 'teacher',
                    badge: 'TEACHER',
                    children: [
                        {
                            id: 'teacher-menu',
                            label: 'Teacher Dashboard',
                            type: 'teacher',
                            expandable: true,
                            children: [
                                { id: 'view-books-t', label: 'View Books', type: 'action' },
                                { id: 'take-books-t', label: 'Take Books', type: 'action' },
                                { id: 'return-books-t', label: 'Return Books', type: 'action' },
                                { id: 'teacher-logout', label: 'Logout', type: 'end' }
                            ]
                        }
                    ]
                },
                {
                    id: 'turn-off',
                    label: 'Turn Off System',
                    type: 'end'
                }
            ]
        }
    ]
};

/**
 * Creates a flowchart node element
 * @param {Object} node - Node data object
 * @returns {HTMLElement} - The created node element
 */
function createNode(node) {
    const nodeDiv = document.createElement('div');
    nodeDiv.className = `flow-node ${node.type} ${node.expandable ? 'expandable' : ''}`;
    nodeDiv.id = node.id;
    nodeDiv.textContent = node.label;

    // Add badge if present
    if (node.badge) {
        const badge = document.createElement('div');
        badge.className = `badge badge-${node.type}`;
        badge.textContent = node.badge;
        nodeDiv.appendChild(badge);
    }

    // Add click handler for expandable nodes
    if (node.expandable) {
        let isExpanded = false;
        nodeDiv.addEventListener('click', function() {
            isExpanded = !isExpanded;
            nodeDiv.classList.toggle('expanded', isExpanded);
            
            const childrenContainer = nodeDiv.parentElement.querySelector('.children-container');
            if (childrenContainer) {
                childrenContainer.classList.toggle('show', isExpanded);
            }
        });
    }

    return nodeDiv;
}

/**
 * Creates a connector line element
 * @returns {HTMLElement} - The created connector element
 */
function createConnector() {
    const connector = document.createElement('div');
    connector.className = 'connector';
    return connector;
}

/**
 * Recursively builds the flowchart structure
 * @param {Object} node - Node data object
 * @param {HTMLElement} container - Container element to append to
 */
function buildFlowchart(node, container) {
    const branch = document.createElement('div');
    branch.className = 'flow-branch';

    // Create and append the node
    const nodeElement = createNode(node);
    branch.appendChild(nodeElement);

    // Process children if present
    if (node.children && node.children.length > 0) {
        branch.appendChild(createConnector());

        if (node.expandable) {
            // Create collapsible container for expandable nodes
            const childrenContainer = document.createElement('div');
            childrenContainer.className = 'children-container';

            if (node.children.length > 1) {
                // Multiple children - create grid layout
                const subActions = document.createElement('div');
                subActions.className = 'sub-actions';
                node.children.forEach(function(child) {
                    subActions.appendChild(createNode(child));
                });
                childrenContainer.appendChild(subActions);
            } else {
                // Single child - recursive build
                buildFlowchart(node.children[0], childrenContainer);
            }

            branch.appendChild(childrenContainer);
        } else {
            if (node.children.length === 1) {
                // Single child - recursive build
                buildFlowchart(node.children[0], branch);
            } else {
                // Multiple children - create horizontal row
                const row = document.createElement('div');
                row.className = 'flow-row';
                node.children.forEach(function(child) {
                    buildFlowchart(child, row);
                });
                branch.appendChild(row);
            }
        }
    }

    container.appendChild(branch);
}

/**
 * Initialize the flowchart when DOM is ready
 */
function initializeFlowchart() {
    const flowchartContainer = document.getElementById('flowchart');
    
    if (flowchartContainer) {
        buildFlowchart(flowData, flowchartContainer);
        console.log('LMS Flowchart initialized successfully');
    } else {
        console.error('Flowchart container not found');
    }
}

// Initialize when DOM is fully loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeFlowchart);
} else {
    initializeFlowchart();
}
