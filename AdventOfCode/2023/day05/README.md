[link](https://adventofcode.com/2023/day/5)

Strategy:
- Do we want to generate all mapping?
    * No, the number are way too big => will take too much 
      memory

Types of Mapping:
- by line: [ Params: num, destination, source, range ]
    * if num between (source, source + range -1):
	* map = destination + (num - source -1)
    * else map = num; has_map = false
- by map: [ Params: num, each rows ]
    * for each row, get mapping
    * if has_map: override; else 

**Prob A**

1. Read Inputs for each seeds; maps
