import pydot
import pytest
import sys
sys.path.append("../")

from prim import (
    fill_nodes_list,
    fill_edge_list,
    generate_graph,
    mst_prim,
    export_graph_from_edgelist,
)


# ---------- Fixtures ----------

@pytest.fixture
def simple_graph():
    graph = pydot.Dot(graph_type="graph")
    graph.add_edge(pydot.Edge("A", "B", weight=1))
    graph.add_edge(pydot.Edge("B", "C", weight=2))
    graph.add_edge(pydot.Edge("A", "C", weight=3))
    return graph


@pytest.fixture
def disconnected_graph():
    graph = pydot.Dot(graph_type="graph")
    graph.add_edge(pydot.Edge("A", "B", weight=1))
    graph.add_node(pydot.Node("C"))
    return graph


# ---------- Tests for fill_nodes_list ----------

def test_fill_nodes_list_adds_all_nodes(simple_graph):
    nodes = []
    fill_nodes_list(simple_graph, nodes)
    assert set(nodes) == {"A", "B", "C"}


def test_fill_nodes_list_no_duplicates(simple_graph):
    nodes = []
    fill_nodes_list(simple_graph, nodes)
    fill_nodes_list(simple_graph, nodes)
    assert len(nodes) == 3


# ---------- Tests for fill_edge_list ----------

def test_fill_edge_list_undirected(simple_graph):
    edgelist = {}
    fill_edge_list(simple_graph, edgelist, is_digraph=False)

    assert "A" in edgelist and "B" in edgelist
    assert ("B", 1.0) in edgelist["A"]
    assert ("A", 1.0) in edgelist["B"]


# ---------- Tests for generate_graph ----------

def test_generate_graph_sorts_nodes(simple_graph):
    nodes, edges = generate_graph(simple_graph)
    assert nodes == sorted(nodes)


def test_generate_graph_returns_edges(simple_graph):
    nodes, edges = generate_graph(simple_graph)
    assert len(edges) > 0


# ---------- Tests for mst_prim ----------

def test_mst_prim_valid_mst(simple_graph):
    nodes, edges = generate_graph(simple_graph)
    mst = mst_prim(nodes, edges)

    total_weight = sum(w for edges in mst.values() for _, w in edges)
    assert total_weight == 3


def test_mst_prim_starts_with_smallest_node(simple_graph):
    nodes, edges = generate_graph(simple_graph)
    nodes.reverse()  # force unsorted input
    nodes.sort()
    mst = mst_prim(nodes, edges)
    assert nodes[0] in mst


def test_mst_prim_with_single_node():
    nodes = ["A"]
    edges = {"A": []}
    mst = mst_prim(nodes, edges)
    assert mst == {"A": []}


# ---------- Edge cases ----------

def test_mst_prim_disconnected_graph(disconnected_graph):
    nodes, edges = generate_graph(disconnected_graph)
    mst = mst_prim(nodes, edges)
    assert "A" in mst


# ---------- Tests for export_graph_from_edgelist ----------

def test_export_graph_from_edgelist():
    edgelist = {"A": [("B", 2.0)]}
    graph = export_graph_from_edgelist(edgelist)

    edges = graph.get_edges()
    assert len(edges) == 1
    assert edges[0].get_source() == "A"
    assert edges[0].get_destination() == "B"
    assert edges[0].get_label() == '"2.0"'
