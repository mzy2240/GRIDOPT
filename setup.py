#*****************************************************#
# This file is part of GRIDOPT.                       #
#                                                     #
# Copyright (c) 2015-2017, Tomas Tinoco De Rubira.    #
#                                                     #
# GRIDOPT is released under the BSD 2-clause license. #
#*****************************************************#

from setuptools import setup

setup(name='GRIDOPT',
      version='1.3.2',
      description='Power Grid Optimization Library',
      author='Tomas Tinoco De Rubira',
      author_email='ttinoco5687@gmail.com',
      packages=['gridopt',
                'gridopt.power_flow',
                'gridopt.stochastic',
                'gridopt.stochastic.two_stage_DCOPF',
                'gridopt.stochastic.multi_stage_DCOPF'],
      scripts=['./gridopt/script/gridopt'],
      install_requires=['scipy',
                        'numpy',
                        'pfnet',
                        'optalg',
                        'multiprocess'])
