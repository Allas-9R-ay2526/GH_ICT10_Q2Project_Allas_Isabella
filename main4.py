from pyscript import display

creator = {
    'name': 'Isabella Allas',
    'tagline': 'Student',
    'about': 'Im a student that likes sketching.',
    'quote': 'Your death is more guaranteed than your wedding day.',
    'quote_by': 'Unknown'
}

interests = ['Sketching', 'Food', 'Books']
hobbies = ['Reading', 'Baking', 'Drawing']
dreams = ['To make a comfortable wage']

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