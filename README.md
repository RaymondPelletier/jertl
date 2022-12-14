<!-- jertl documentation master file, created by
sphinx-quickstart on Mon Oct 17 12:15:46 2022.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# jertl - A minimum viable package for processing structured data

Where developers declaratively define and execute common operations on complex data structures.

Operations are specified using a mini-language in which target structures are visually similar to their textual representation.

## Examples

### Matching

Jertl can be used to verify the structure of data, select nested values, or both.

```python
>>> movie = {"title": "Pinocchio", "MPAA rating": "PG"}
>>>
>>> match = jertl.match('{"title": title, "MPAA rating": "PG"}', movie)
>>>
>>> if match is not None:
...     print(match.bindings['title'])
...
Pinocchio
```

### Filling

Jertl can also be used as a template library.

```python
>>> jertl.fill('{"name": name, "age": age, "status": status}',
...            name="Ray",
...            age=66,
...            status='employed')
{'name': 'Ray', 'age': 66, 'status': 'employed'}
```

### Transforming

Data transformations are defined using representations of the source and target data.

```python
>>> retire = '{"status": "employed", **the_rest} --> {"status": "retired", **the_rest}'
>>>
>>> ray = {'name': 'Ray', 'age': 66, 'status': 'employed'}
>>>
>>> transformation = jertl.transform(retire, ray)
>>> transformation.filled
{'status': 'retired', 'name': 'Ray', 'age': 66}
```

### Collating

You can use Jertl to verify relationships between data structures.

```python
>>> supervises = '''
...     supervisor ~ {"underlings": [*_, name, *_]}
...     employee   ~ {"name": name}
...     '''
>>>
>>> jeremy = {'name': 'Jeremy'}
>>> jeff   = {'name': 'Jeff', 'underlings': ['Jimmy', 'Johnny', 'Jeremy', 'Joe']}
>>>
>>> collation = jertl.collate(supervises, supervisor=jeff, employee=jeremy)
>>> collation is not None
True
```

### Inferring

Combining all these operations gives you an inference engine.

```python
>>> rule = '''
...    //
...    // Create a list of movies with their ratings explained
...    //
...    movies       ~ [*_, {"title": title, "MPAA rating": rating},        *_]
...    MPAA_ratings ~ [*_, {"rating": rating, "explanation": explanation}, *_]
... -->
...    movie       := {"title": title, "contents": explanation}
...'''
...
>>> movies = [{'title': 'Toy Story',                          'MPAA rating': 'G'},
...           {'title': 'South Park: Bigger, Longer & Uncut', 'MPAA rating': 'NC-17'}]
...
>>> MPAA_ratings = [{'rating':      'G',
...                  'summary':     'GENERAL AUDIENCES',
...                  'explanation': 'Nothing to offend parents for viewing by children.'},
...                 {'rating':      'PG',
...                  'summary':     'PARENTAL GUIDANCE SUGGESTED',
...                  'explanation': 'May contain some material parents might not like for their young children'},
...                 {'rating':      'PG-13',
...                  'summary':     'PARENTS STRONGLY CAUTIONED',
...                  'explanation': 'Some material may be inappropriate for pre-teens.'},
...                 {'rating':      'R',
...                  'summary':     'RESTRICTED',
...                  'explanation': 'Contains some adult material.'},
...                 {'rating':      'NC-17',
...                  'summary':     'NO ONE 17 AND UNDER ADMITTED',
...                  'explanation': 'Clearly for adults only.'}]
...
>>> for inference in jertl.infer_all(rule, movies=movies, MPAA_ratings=MPAA_ratings):
...     print(inference.fills['movie'])
...
{'title': 'Toy Story', 'contents': 'Nothing to offend parents for viewing by children.'}
{'title': 'South Park: Bigger, Longer & Uncut', 'contents': 'Clearly for adults only.'}
```

## Installation

```bash
pip install jertl
```
