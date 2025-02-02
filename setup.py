#!/usr/bin/env python

# offset-finder
#
# Copyright (c) 2014 British Broadcasting Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='audio-offset-finder',
    version='0.3.0',
    description='Find the offset of an audio file within another audio file',
    author='Yves Raimond, Calder White',
    author_email='calderwhite1@gmail.com',
    url='https://github.com/CalderWhite/audio-offset-finder',
    license='Apache License 2.0',
    packages=['audio_offset_finder'],
    install_requires=[
        'scipy>=0.12.0',
        'numpy',
        'scikits.talkbox', 
    ],
    scripts=['bin/audio-offset-finder'],
)

