#!/usr/bin/ruby
require 'open-uri'
require 'JSON'

query = ARGV[0]
output = Array.new
results = JSON.parse(open("http://search.cocoapods.org/api/v1.5/pods/search?query=#{query}").read)

results.each do |item|
    hash = Hash.new
    hash["title"] = item["id"]+" "+item["version"]
    hash["subtitle"] = item["summary"]
    hash["url"] = "http://cocoadocs.org/docsets/#{item['id']}/#{item['version']}"
    output.push(hash)
end

puts output.to_json