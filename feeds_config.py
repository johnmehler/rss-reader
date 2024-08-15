FEEDS = [
    {
        'url': 'https://innermammal.substack.com/feed',
        'source': 'Inner Mammal Substack',
        'source_url': 'https:///innermammal.substack.com',  # Extracted URL
        'image_xpath': './media:content',  # Adjust if necessary
        'image_ns': {'media': 'http:/search.yahoo.com/mrss/'},  # Namespace for media:content
        'content_xpath': './content:encoded',
        'content_ns': {'content': 'http:/purl.org/rss/1.0/modules/content/'}
    },
    {
        'url': 'https://hedgehogreview.com/web-features/feed',
        'source': 'Hedgehog Review',
        'source_url': 'https://hedgehogreview.com/',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {},
        'content_xpath': './content:encoded',
        'content_ns': {'content': 'http:/purl.org/rss/1.0/modules/content/'}
    },
    {
        'url': 'https://mcrawford.substack.com/feed',
        'source': 'M.B. Crawford Substack',
        'source_url': 'https://mcrawford.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://freddiedeboer.substack.com/feed',
        'source': 'Freddie deBoer Substack',
        'source_url': 'https://freddiedeboer.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://mattdinan.substack.com/feed',
        'source': 'Matt Dinan Substack',
        'source_url': 'https://mattdinan.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    # {
    #     'url': 'https://feeds.feedblitz.com/marginalrevolution',
    #     'source': 'Marginal Revolution',
    #     'source_url': 'https://feeds.feedblitz.com/marginalrevolution',  # Extracted URL
    #     'image_xpath': './enclosure',
    #     'image_ns': {}
    # },
    {
        'url': 'https://samkriss.substack.com/feed',
        'source': 'Sam Kriss Substack',
        'source_url': 'https://samkriss.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://garymarcus.substack.com/feed',
        'source': 'Gary Marcus Substack',
        'source_url': 'https://garymarcus.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://marygaitskill.substack.com/feed',
        'source': 'Mary Gaitskill Substack',
        'source_url': 'https://marygaitskill.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://seymourhersh.substack.com/feed',
        'source': 'Seymour Hersh Substack',
        'source_url': 'https://seymourhersh.substack.com',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://thereveal.substack.com/feed',
        'source': 'The Reveal',
        'source_url': 'https://thereveal.substack.com/',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://theconvivialsociety.substack.com/feed',
        'source': 'Convivial Society',
        'source_url': 'https://theconvivialsociety.substack.com/',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://democracyforsale.substack.com/feed',
        'source': 'Democracy For Sale',
        'source_url': 'https://democracyforsale.substack.com/',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    },
    {
        'url': 'https://coolstuffnyc.substack.com/feed',
        'source': 'Cool Stuff NYC',
        'source_url': 'https:///coolstuffnyc.substack.com/',  # Extracted URL
        'image_xpath': './enclosure',
        'image_ns': {}
    }
]
