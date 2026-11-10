from pyscript import display

creator = {
    'name': 'Cean Alagar',
    'tagline': 'Student, Racer, and curious about things.',
    'about': 'Im a curous person that likes racing. I also like living life along the edge meaning doing things that somepople dont like to do like     skydiving.',
    'quote': 'You can only get over your fears if you attack them head on.',
    'quote_by': 'Mika Häkkinen'
}

interests = ['Go karting', 'F1', 'Cars']
hobbies = ['Racing', 'kart racing', 'playing games']
dreams = ['To get in mapua ']

quote = creator.get('quote')
quote_by = creator.get('quote_by')

display('Meet Me', target='output')
display(creator.get('name'), target='output')
display(creator.get('tagline'), target='output')

display('About me', target='output')
display(creator.get('about'), target='output')

display('Interests', target='output')
display(', '.join(interests), target='output')

display('Hobbies', target='output')
display(', '.join(hobbies), target='output')

display('Dreams', target='output')
display(', '.join(dreams), target='output')

display(f'"{quote}" - {quote_by}', target='output')