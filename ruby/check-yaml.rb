#!/usr/bin/ruby
#### usage  ruby chechk-yaml.rb file.yaml [file2.yaml ...]

require 'yaml'
require 'pp'

str  = ARGF.read()      # Read Intut
data = YAML.load(str)   # Pares
pp data                 # print
