import unittest

import networkx as nx
from streamlit.testing.v1 import AppTest

from core.search_algorithms import bfs, dfs
from search_simulation import GRAPH


class SearchTests(unittest.TestCase):
    def test_default_orders_and_frontiers(self):
        breadth = bfs(GRAPH, 'A', 'G')
        depth = dfs(GRAPH, 'A', 'G')
        self.assertEqual(breadth.visited_order, list('ABCDEFG'))
        self.assertEqual(depth.visited_order, list('ABDECFG'))
        for result in (breadth, depth):
            self.assertEqual(result.path, list('ACG'))
            self.assertEqual(result.history[0].frontier, ['A'])
            self.assertEqual(result.history[0].visited_order, [])
        self.assertEqual(breadth.history[1].frontier, list('BC'))
        self.assertEqual(breadth.history[2].frontier, list('CDE'))
        self.assertEqual(depth.history[1].frontier, list('CB'))
        self.assertEqual(depth.history[2].frontier, list('CED'))

    def test_all_pairs(self):
        for search in (bfs, dfs):
            for start in GRAPH:
                for goal in GRAPH:
                    with self.subTest(search=search.__name__, start=start, goal=goal):
                        result = search(GRAPH, start, goal)
                        self.assertEqual(result, search(GRAPH, start, goal))
                        self.assertEqual(result.path, nx.shortest_path(nx.Graph(GRAPH), start, goal))
                        self.assertEqual(len(result.visited_order), len(set(result.visited_order)))
                        for index, step in enumerate(result.history):
                            self.assertEqual(step.visited_order, result.visited_order[:index])
                            self.assertFalse(set(step.frontier) & set(step.visited_order))
                            self.assertEqual(len(step.frontier), len(set(step.frontier)))
                        if start == goal:
                            self.assertEqual(result.path, [start])
                            self.assertEqual(len(result.history), 2)

    def test_cycles_disconnected_invalid_and_nonshortest_dfs(self):
        graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'G'],
                 'D': ['B', 'E'], 'E': ['D', 'G'], 'G': ['C', 'E'], 'Z': []}
        self.assertEqual(bfs(graph, 'A', 'G').path, list('ACG'))
        self.assertEqual(dfs(graph, 'A', 'G').path, list('ABDEG'))
        for search in (bfs, dfs):
            result = search(graph, 'A', 'Z')
            self.assertEqual(result.path, [])
            self.assertEqual(result.history[-1].frontier, [])
            self.assertEqual(len(result.visited_order), len(set(result.visited_order)))
            with self.assertRaises(ValueError):
                search(graph, 'INVALID', 'A')


class InterfaceTests(unittest.TestCase):
    def test_navigation_steps_and_reset(self):
        at = AppTest.from_file('app.py', default_timeout=20).run()
        for unit in range(10):
            at.selectbox(key='selected_unit').select(unit).run()
            self.assertFalse(at.exception)
            if unit != 1:
                self.assertEqual(at.info[0].value, 'Simulation coming soon')
                self.assertEqual(len(at.slider), 0)
        at.selectbox(key='selected_unit').select(1).run()
        for algorithm in ('BFS', 'DFS'):
            at.selectbox(key='search_algorithm').select(algorithm).run()
            self.assertEqual(at.slider[0].value, 0)
            for step in range(8):
                at.slider[0].set_value(step).run()
                self.assertFalse(at.exception)
                self.assertEqual(len(at.success), 1 if step == 7 else 0)
                self.assertTrue(any(f'**{"Queue" if algorithm == "BFS" else "Stack"}:**' in m.value for m in at.markdown))
        for start, goal in [('G', 'D'), ('D', 'A'), ('C', 'C')]:
            at.selectbox(key='search_start').select(start).run()
            at.selectbox(key='search_goal').select(goal).run()
            self.assertEqual(at.slider[0].value, 0)
            at.slider[0].set_value(at.slider[0].max).run()
            self.assertFalse(at.exception)
            self.assertEqual(len(at.success), 1)
        self.assertTrue(any('**จำนวนเส้นเชื่อม (Number of edges):** 0' == m.value for m in at.markdown))


if __name__ == '__main__':
    unittest.main()
