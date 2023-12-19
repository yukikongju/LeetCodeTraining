# define c++ compiler
CXX = g++

# define source and output files
cpp_file = BuildingTeams.cpp
# cpp_file = ShortestRoutesII.cpp
output_file = a.out
# input_file = inputs/ShortestRoutesII.in
input_file = inputs/BuildingTeams.in

# define compile flags
CXXFLAGS = -std=c++11 -Wall

# compile: $(output_file) $(cpp_file)
	# $(CXX) $(CXXFLAGS) -o  $@ $<

compile:
	$(CXX) $(cpp_file) -o $(output_file)

run:
	$(CXX) $(cpp_file) -o $(output_file)
	./$(output_file) < $(input_file)


clean: 
	rm $(output_file)


