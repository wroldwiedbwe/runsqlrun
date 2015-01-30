commands = {
    'app': {
        'label': 'Application',
        'actions': {
            'neweditor': {
                'label': 'New SQL editor',
                'description': 'Open new SQL editor',
                'icon': 'document-new-symbolic',
                'shortcut': '<Control>N',
                'callback': 'win.docview.add_worksheet'
            },
            'switch_editor1': {
                'label': 'Switch to editor 1',
                'shortcut': '<Alt>1',
                'callback': 'win.docview.switch_to_editor',
                'args': [1]
            },
            'switch_editor2': {
                'label': 'Switch to editor 2',
                'shortcut': '<Alt>2',
                'callback': 'win.docview.switch_to_editor',
                'args': [2]
            },
            'switch_editor3': {
                'label': 'Switch to editor 3',
                'shortcut': '<Alt>3',
                'callback': 'win.docview.switch_to_editor',
                'args': [3]
            },
            'switch_editor4': {
                'label': 'Switch to editor 4',
                'shortcut': '<Alt>4',
                'callback': 'win.docview.switch_to_editor',
                'args': [4]
            },
            'switch_editor5': {
                'label': 'Switch to editor 5',
                'shortcut': '<Alt>5',
                'callback': 'win.docview.switch_to_editor',
                'args': [5]
            },
            'switch_editor6': {
                'label': 'Switch to editor 6',
                'shortcut': '<Alt>6',
                'callback': 'win.docview.switch_to_editor',
                'args': [6]
            },
            'switch_editor7': {
                'label': 'Switch to editor 7',
                'shortcut': '<Alt>7',
                'callback': 'win.docview.switch_to_editor',
                'args': [7]
            },
            'switch_editor8': {
                'label': 'Switch to editor 8',
                'shortcut': '<Alt>8',
                'callback': 'win.docview.switch_to_editor',
                'args': [8]
            },
            'switch_editor9': {
                'label': 'Switch to editor 9',
                'shortcut': '<Alt>9',
                'callback': 'win.docview.switch_to_editor',
                'args': [9]
            }
        }
    },
    'editor': {
        'label': 'SQL Editor',
        'actions': {
            'run': {
                'label': 'Run SQL statement',
                'description': 'Run SQL statement at cursor',
                'icon': 'media-playback-start-symbolic',
                'shortcut': '<Control>Return',
                'callback': 'run_query'
            }
        }
    }
}
