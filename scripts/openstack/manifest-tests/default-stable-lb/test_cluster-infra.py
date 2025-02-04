#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
import glob
import yaml

ASSETS_DIR = ""

class TestClusterInfraObject(unittest.TestCase):
    def setUp(self):
        """Parse the Cluster Infrastructure object into a Python data structure."""
        self.machines = []
        cluster_infra = f'{ASSETS_DIR}/manifests/cluster-infrastructure-02-config.yml'
        with open(cluster_infra) as f:
            self.cluster_infra = yaml.load(f, Loader=yaml.FullLoader)

    def test_load_balancer(self):
        """Assert that the Cluster infrastructure object does not contain the LoadBalancer configuration."""
        self.assertNotIn("loadBalancer", self.cluster_infra["status"]["platformStatus"]["openstack"])


if __name__ == '__main__':
    ASSETS_DIR = sys.argv.pop()
    unittest.main(verbosity=2)
