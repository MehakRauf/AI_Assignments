import tkinter as tk 
from tkinter import ttk 

def create_button_labels(self):
        self.lbl_nodes = tk.Label(self.gui, text="Enter the nodes separated by commas:")  
        self.lbl_nodes.pack()  
        self.nodes_entry = ttk.Entry(self.gui)  
        self.nodes_entry.pack()  

        self.lbl_edges = ttk.Label(self.gui, text="Enter edges as ((from_node-to_node-weight)A-B-30)")  
        self.lbl_edges.pack()  
        self.edges_entry = ttk.Entry(self.gui)  
        self.edges_entry.pack()  

        self.lbl_start_node = ttk.Label(self.gui, text="Enter the initial Node:")  
        self.lbl_start_node.pack()  
        self.start_node_entry = ttk.Entry(self.gui)  
        self.start_node_entry.pack() 

        self.lbl_goal_node = ttk.Label(self.gui, text="Goal Node:")  
        self.lbl_goal_node.pack() 
        self.goal_node_entry = ttk.Entry(self.gui)  
        self.goal_node_entry.pack()  

        self.lbl_max_steps = ttk.Label(self.gui, text="Maximum Steps:")  
        self.lbl_max_steps.pack()  
        self.max_steps_entry = ttk.Entry(self.gui)  
        self.max_steps_entry.pack()  

        self.search_algo_frame = ttk.Frame(self.gui) 
        self.search_algo_frame.pack(side=tk.TOP, padx=10, pady=10)  

        self.btn_bfs = ttk.Button(self.search_algo_frame, text="Breadth-First Search (BFS)", command=self.breadth_first_search)  
        self.btn_bfs.pack(side=tk.LEFT, padx=5, pady=5) 

        self.btn_ucs = ttk.Button(self.search_algo_frame, text="Uniform Cost Search (UCS)", command=self.uniform_cost_search)  
        self.btn_ucs.pack(side=tk.LEFT, padx=5, pady=5) 

        self.btn_dfs = ttk.Button(self.search_algo_frame, text="Depth-First Search (DFS)", command=self.depth_first_search)  
        self.btn_dfs.pack(side=tk.LEFT, padx=5, pady=5)  

        self.btn_iddfs = ttk.Button(self.search_algo_frame, text="Iterative Deepening DFS (IDDFS)", command=self.iterative_deepening_dfs) 
        self.btn_iddfs.pack(side=tk.LEFT, padx=5, pady=5) 

        self.btn_random = ttk.Button(self.search_algo_frame, text="Random Search", command=self.random_explore)  
        self.btn_random.pack(side=tk.LEFT, padx=5, pady=5)  

        self.btn_random = ttk.Button(self.search_algo_frame, text="Random Search with open and closed list", command=self.random_open_closed_list)  
        self.btn_random.pack(side=tk.LEFT, padx=5, pady=5)  
        
        style_frames(self)  
        
def style_frames(self):
            self.search_algo_frame.configure(relief=tk.RIDGE, borderwidth=4, style="SearchAlgo.TFrame")  
            self.gui.style = ttk.Style()  
            self.gui.style.configure("SearchAlgo.TFrame", background="light blue", padx=20, pady=20)  # Configure the 
