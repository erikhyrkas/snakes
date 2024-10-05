# todo: extract data from text

# prompt structure:
# "given this form/paragraph, extract the data as csv/json/markdown/yaml"
#
# generation method:
# * use the "data_generator_format.py"'s logic to generate data, then ask llama 3.1 to make a form or paragraph of text
#   using all provided data.
# *then flip it around, where the form becomes part of the query and the generated data is the answer. There's a little
#   risk that llama 3 will not include all of the original data, but otherwise this is simple enough.