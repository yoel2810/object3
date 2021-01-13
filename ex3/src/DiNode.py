class DiNode:

    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        self.out_edges = {}
        self.in_edges = {}
        self.info = ""
        self.weight = 2147483647.0
        self.tag = 0
        self.pos = pos

    def get_id(self) -> int:
        return self.id

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_info(self):
        return self.info

    def get_tag(self) -> int:
        return self.tag

    def get_pos(self) -> tuple:
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def get_in_edges(self):
        return self.in_edges

    def get_out_edges(self):
        return self.out_edges

    def __str__(self):
        return  (self.id + ": |edges out| " + str(len(self.out_edges)) + " |edges in| " + str(len(self.in_edges)))
