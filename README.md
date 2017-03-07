# pixelmap

A map of Pixel data structures.

## Getting Started

Follow these instructions to get started using and developing pixelmap.

### Tools

Some things you you'll need

* [pip](https://packaging.python.org/installing/#creating-and-using-virtual-environments) - Python package manager
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - Isolated environment

### Installing

Once you have a virtualenv set up, run these commands to install

```
$ git clone https://github.com/yebra06/pixelmap.git
$ cd pixelmap
$ pip install -r requirements.txt . # Install all dependencies
```

### Usage

```bash
$ python
```
```python
>>> from pixelmap import pixelmap
>>>
>>> def create_pixelmap():
...     pmap = pixelmap.Pixelmap(5,5)
...     print pmap
...
>>> create_pixelmap()
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
```

## Testing

Currently using [pytest](http://doc.pytest.org/en/latest/) - Python test framework

### Example

```bash
$ pytest tests
```

## Get involved

If you would like to contribute:
* Create a fork and start hacking and submit a pull request!

### License - MIT
- [MIT License](https://github.com/yebra06/pixelmap/blob/master/LICENSE)
- Submit any bugs or issues you have.