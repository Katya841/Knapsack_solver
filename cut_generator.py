from mip import ConstrsGenerator, xsum, Model

class OddConstraintCutGenerator(ConstrsGenerator):
    
    def __init__(self):
        super().__init__()
        self.calls = 0  # Initialize the call counter

    def generate_constrs(self, model: Model, depth: int = 0, npass: int = 0):
        self.calls += 1
       
        selected_indices = [i for i, var in enumerate(model.vars) if var.x >= 0.99]
        num_selected = len(selected_indices)
        if num_selected % 2 == 0 and num_selected > 0:
            cut =  xsum(model.vars[i] for i in selected_indices) <= num_selected - 1
            model.add_cut(cut)

