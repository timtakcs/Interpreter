import Parser as prs
import Lexer as lx
import Error as err

#Visiting pattern
#this is awful - do some string concetenation for functions
class Visitor(object):
    def visit(self, node):
        if isinstance(node, prs.FactorNode):
            return self.visitNumNode(node)
        elif isinstance(node, prs.OperatorNode):
            return self.visitOpNode(node)
        elif isinstance(node, prs.CompoundStmtNode):
            return self.visitCompNode(node)
        elif isinstance(node, prs.AssignmentNode):
            return self.visitAssgnNode(node)
        elif isinstance(node, prs.VariableNode):
            return self.visitVarNode(node)
        elif isinstance(node, prs.IfNode):
            return self.visitIfNode(node)
        elif isinstance(node, prs.LogicNode):
            return self.visitLogicNode(node)
        elif isinstance(node, prs.ForNode):
            return self.visitForNode(node)

#Interpreter

class Interpreter(Visitor):
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}

    def visitOpNode(self, node):
        if node.operator.type == lx.typePlus:
            return self.visit(node.leftChild) + self.visit(node.rightChild)
        elif node.operator.type == lx.typeMinus:
            return self.visit(node.leftChild) - self.visit(node.rightChild)
        elif node.operator.type == lx.typeMultiply:
            return self.visit(node.leftChild) * self.visit(node.rightChild)
        elif node.operator.type == lx.typeDivide:
            return self.visit(node.leftChild) / self.visit(node.rightChild)

    def visitNumNode(self, node):
        return node.value.value

    #TODO this doesnt like assignign strings to variables, fix it
    def visitVarNode(self, node):
        if node.value not in self.variables:
            return None, err.MissingVariableError(node.token.line)
        return self.variables[node.value]
        
    def visitAssgnNode(self, node):
        print(node)
        self.variables[node.leftChild.value] = self.visit(node.rightChild)

    def visitCompNode(self, node):
        results = []

        for stmt in node.statements:
            results.append(self.visit(stmt))
        
        return results     

    #TODO && and || interpreting
    def visitLogicNode(self, node):
        if node.operator.type == lx.typeEQL:
            return self.visit(node.leftChild) == self.visit(node.rightChild)
        elif node.operator.type == lx.typeLessEql:
            return self.visit(node.leftChild) <= self.visit(node.rightChild)
        elif node.operator.type == lx.typeGrtrEql:
            return self.visit(node.leftChild) >= self.visit(node.rightChild)
        elif node.operator.type == lx.typeLess:
            return self.visit(node.leftChild) < self.visit(node.rightChild)
        elif node.operator.type == lx.typeGreater:
            return self.visit(node.leftChild) > self.visit(node.rightChild)

    def visitIfNode(self, node):
        for condition, expr in node.cases:
            if self.visit(condition) == True:
                return self.visit(expr)
        if node.elseCase != None:
            return self.visit(node.elseCase)

    def visitForNode(self, node):
        self.visit(node.counter)

        while self.visit(node.limit) == True:
            self.visit(node.body)
            self.visit(node.step)

    def interpret(self):
        self.tree = self.parser.parse()
        print(self.tree)
        self.visit(self.tree.node)
        return self.variables
