from mediawiki import MediaWiki

wiki = MediaWiki(url='https://oldschool.runescape.wiki/api.php')
npcs = wiki.categorymembers('Non-player_characters', 9001)
for npc in npcs[0]:
    print(npc)