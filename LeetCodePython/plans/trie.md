🟩 1. Classic Trie – Prefix Insert / Search

Operations: Insert word, search word, startsWith (prefix check)

Use Case: Fast lookup of words / prefixes in O(L) time, L = word length

Problems

Implement Trie (Prefix Tree) – 208. Implement Trie (Prefix Tree)

Add and Search Word – 211. Add and Search Word - Data structure design

Replace Words – 648. Replace Words

Pattern

Each node contains children and is_end flag

Traverse character by character

Optional: store word or extra info at node

🟦 2. Word / Prefix Matching

Operations: Check if any word starts with prefix / autocomplete

Use Case: Autocomplete, suggestions

Problems

Search Suggestions System – 1268. Search Suggestions System

Map Sum Pairs – 677. Map Sum Pairs

Design Add and Search Words Data Structure – 211

Pattern

Traverse prefix in Trie

Use DFS / BFS to collect words starting from the prefix node

Return top-k lexicographical or largest sum

🟥 3. Palindrome / Reverse Word Problems

Operations: Check for palindromes using Trie of reversed words

Use Case: Find palindrome pairs efficiently

Problems

Palindrome Pairs – 336. Palindrome Pairs

Shortest Reference String (Minimum Length Encoding) – 820. Short Encoding of Words

Pattern

Insert words in reverse order

While searching, check if prefix / suffix forms a palindrome

Store indices or special info at nodes for O(1) lookup

🟨 4. Multi-key / Character Mapping

Operations: Trie with custom alphabet or extended character set

Use Case: Phone digits to words, URL paths, encoding

Problems

Implement Trie for lowercase, uppercase, digits – e.g., Design Search Autocomplete System – 642. Design Search Autocomplete System

Replace Words with dictionary

File System / Folder hierarchy – 1233. Remove Sub-Folders from the Filesystem

Pattern

Each node has children map (dict) instead of fixed array

DFS to traverse all children

Handle end-of-word markers

🟪 5. Grid / Board / DFS using Trie

Operations: Search words on a 2D board using Trie for prefix pruning

Use Case: Efficient word search / path search

Problems

Word Search II – 212. Word Search II

Boggle / Dictionary Search variants

Pattern

Insert all words into Trie

DFS on board: prune search using Trie prefix

Mark visited cells to avoid cycles

🟫 6. Bitwise / Optimization / Compressed Trie

Operations: Bitwise Trie / Binary Trie for integers

Use Case: Max XOR, subset queries

Problems

Maximum XOR of Two Numbers in an Array – 421. Maximum XOR of Two Numbers in an Array

Count of Range Sum (advanced optimization)

Pattern

Trie node represents bit 0 or 1 instead of character

Insert numbers in binary

Use XOR properties to traverse for max value

🟧 7. Frequency / Sum / Map Trie

Operations: Trie nodes store cumulative sum or count

Use Case: Prefix sums for strings / integer keys

Problems

Map Sum Pairs – 677. Map Sum Pairs

Count Prefixes / Frequency queries

Pattern

Each node stores sum or count

When inserting, update sum along path

Query prefix sum / frequency by traversing prefix node
