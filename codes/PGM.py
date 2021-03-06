from libpgm.graphskeleton import GraphSkeleton
from libpgm.nodedata import NodeData
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.tablecpdfactorization import TableCPDFactorization


def getTableCPD():
    nd = NodeData()
    skel = GraphSkeleton()
    jsonpath = "./graph/graph_example.txt"
    nd.load(jsonpath)
    skel.load(jsonpath)
    # load Bayesian network
    bn = DiscreteBayesianNetwork(skel, nd)
    tablecpd = TableCPDFactorization(bn)
    return tablecpd

# Casual Reasoning
tcpd = getTableCPD()
print tcpd.specificquery(dict(Offer='1'), dict(Grades='0'))
tcpd = getTableCPD()
print tcpd.specificquery(dict(Offer='1'), dict(Grades='0', Experience='0'))

# Evidential Reasoning
tcpd = getTableCPD()
print tcpd.specificquery(dict(Experience='1'), dict())
tcpd = getTableCPD()
print tcpd.specificquery(dict(Experience='1'), dict(Interview='2'))

# inter-casual
tcpd = getTableCPD()
print tcpd.specificquery(dict(Experience='1'), dict())
tcpd = getTableCPD()
print tcpd.specificquery(dict(Experience='1'), dict(Interview='2'))
tcpd = getTableCPD()
print tcpd.specificquery(dict(Experience='1'), dict(Interview='2', Grades='0'))

