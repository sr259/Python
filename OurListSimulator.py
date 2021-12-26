#########################################################
#
# NOTE: You should not examine any of this source code.
#
# Just execute it for the simulation.
#
#
#########################################################

from random import *
from copy import *
from string import ascii_uppercase

def padWithUnique(l, n):
  while len(l) < n:
    temp = choice(ascii_uppercase)
    while temp not in l:
      l.append(temp)

def nonmatch(c):
  temp = c
  while temp == c:
    temp = choice(ascii_uppercase)
  return temp

class OurListSimulator:

  
  def isEmptyCase(self, r=None):
    NUM_CASES = 2
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    if r > 0: # Not empty
      l.append(choice(ascii_uppercase))
    return (l, 'data._isEmpty()', l._isEmpty(), deepcopy(l))
    
  def lenCase(self, r=None):
    NUM_CASES = 3   # simulate non-empty 2/3 of the time
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    if r > 0: # Not empty
      padWithUnique(l, randint(0,10))
    return (l, 'data.__len__()     a.k.a. len(data)', len(l), deepcopy(l))
    
  def containsCase(self, r=None):
    NUM_CASES = 4
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    searchElement = choice(ascii_uppercase)
    if r == 0:    # Empty
      pass
    elif r == 1:  # At the head
      l.append(searchElement)
    elif r >= 2:  # Mismatch at head (possible match in rest)
      l.append(nonmatch(searchElement))
      if r == 3: # also put a match on sublist so it says True
        l.append(searchElement)
    return (l, f"data.__contains__('{searchElement}')     a.k.a. '{searchElement}' in data", searchElement in l, deepcopy(l))
      
  def getItemCase(self, r=None):
    NUM_CASES = 4
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    if r == 0:    # empty list (and query that is IndexError)
      itemIndex = randint(0,5)
    elif r > 0:
      if r == 1:  # Ask for index 0
        itemIndex = 0
      else:
        itemIndex = randint(1,5)
      padWithUnique(l, 20)

    msg = f"data.__getitem__({itemIndex})     a.k.a. data[{itemIndex}]"
    if itemIndex < len(l):
      return (l, msg, l[itemIndex], deepcopy(l))
    else:
      return (l, msg, 'IndexError', deepcopy(l))

  def countCase(self, r=None):
    NUM_CASES = 5
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    if r == 0:    # empty list (and query that is IndexError)
      target = choice(ascii_uppercase)
    elif r in (1,2):
      # match at head, and possibly more matches that follow
      padWithUnique(l,10)
      target = l[0]
      if r == 2:
        for _ in range(randint(1,5)):
          l.append(target)
    elif r in (3,4):
      # no match at head, and possibly more matches that follow
      padWithUnique(l,10)
      target = l[len(l)-1]
      l.remove(target)
      if r == 4:
        for _ in range(randint(1,5)):
          l.append(target)

    return (l, f"data.count('{target}')", l.count(target), deepcopy(l))

  def indexCase(self, r=None):
    NUM_CASES = 4
    if r is None:
      r = randint(0,NUM_CASES-1)
    else:
      r = r % NUM_CASES
      
    l = OurList()
    item = choice(ascii_uppercase) # default choice
    
    if r > 0:
      padWithUnique(l, 6)
      if r == 1:  # Ask for what is at index 0
        j = 0
        item = l[j]
      elif r == 2:
        j = randint(1,5)  # valid index
        item = l[j]
      else:
        j = randint(6,9)  # invalid index

    msg = f"data.index('{item}')"
    if r in (1,2):
      return (l, msg, j, deepcopy(l))
    else:
      return (l, msg, 'IndexError', deepcopy(l))

  def appendCase(self, r=None):
    if r is None:
      r = randint(0,2)
    else:
      r = r % 2
      
    l = OurList()
    
    if r == 0: # Sentry node
      pass
    else:
      l.append(choice(ascii_uppercase))
      
    result = deepcopy(l)
    newItem = choice(ascii_uppercase)
    result.append(newItem)
    
    return (l, f'append({newItem})', None, result)
    
  def run(self, case):
    (self._current, self._call, self._correctResult, self._after) = case
    print('='*40)
    print('Challenge: Determine the result of the call to the member function:')
    print(f'  {self._call}')
    print()
    print('Current list state:')
    print(f'  _head = {self._current._head}')
    if self._current._rest is None:
      print('  _rest = None')
    else:
      print(f'  _rest = OurList instance with id {id(self._current._rest) % 100000}')
    print('='*40)
    done = False
    while not done:
      response = self._mainMenu()
      
      if response == 1:
        self._functionCall()
      elif response == 2:
        validResponse = False
        while not validResponse:
          response = input('Enter the return value: ')
          if response.strip().lower() == 'true':
            self._result = True
            validResponse = True
          elif response.strip().lower() == 'false':
            self._result = False
            validResponse = True
          else:
            try:
              self._result = int(response)
              validResponse = True
            except ValueError:
              if len(response.strip()) == 1:
                self._result = response.upper()
                validResponse = True
          if not validResponse:
            print('Enter an appropriate integer, character, True, or False')
        done = True
      elif response == 3:
        self._result = None
        done = True
      elif response == 4:
        self._setHead()
      elif response == 5:
        self._newRest()
      elif response == 6:
        self._result = self._getException()
        done = True
        
    print()
    correct = True
    if self._result != self._correctResult or type(self._result) != type(self._correctResult):
      print('='*40)
      print('Challenge outcome: Unsuccessful')
      print('  You provided the wrong return value')
      print('  You returned',self._result)
      print('  Expected return was',self._correctResult)
      print('='*40)
      correct = False
    if self._current != self._after:
      print('='*40)
      print('Challenge outcome: Unsuccessful')
      print('  Your list has the incorrect state')
      print('='*40)
      correct = False
    if correct:
      print('='*40)
      print('Challenge outcome: success')
      print('='*40)
      
  def _mainMenu(self):
    print()
    print('Your options are:')
    print('  1) Call a member function for _rest')
    print('  2) Exit from the function while providing a return value')
    print('  3) Exit from the function returning None')
    print('  4) Set the value of _head')
    print('  5) Set _rest to a new OurList instance')
    print('  6) Raise an exception')
    print()
    validResponse = False
    while not validResponse:
      response = input('What would you like to do?  (Enter a number) ')
      try:
        response = int(response)
        if 1 <= response <= 6:
          validResponse = True
      except ValueError:
        print('Enter a number between 1 an 6')
    return response
    
  def _functionCall(self):
    # don't love that this is still so hard wired, but for now...
    print('What function would you like to call?')
    print('  1)  _rest._isEmpty()')
    print('  2)  _rest.__len__()')
    print('  3)  _rest.__contains__(value)')
    print('  4)  _rest.__getitem__(index)')
    print('  5)  _rest.count(value)')
    print('  6)  _rest.index(value)')
    print('  7)  _rest.append(value)')
    print()
    N = 7
    validResponse = False
    while not validResponse:
      response = input('What would you like to do?  (Enter a number) ')
      try:
        response = int(response)
        if 1 <= response <= N:
          validResponse = True
      except ValueError:
        print(f'Enter a number between 1 an {N}')
        
    if response in [3,5,6,7]:   # value base
      validValue = False
      while not validValue:
          value = input('Parameter to send: ').strip().strip('"').strip("'").upper() # remove whitespace and quotes
          if len(value)==1 and value.isalpha():
              validValue = True
          else:
              print('Enter a single letter')
    if response in [4]:       # index based
      validIndex = False
      while not validIndex:
        try:
          index = int(input('Parameter to send: '))
          validIndex = True
        except ValueError:
          print('Enter an integer')
    
    try:
      if response == 1:
        returnValue = self._current._rest._isEmpty()
      if response == 2:
        returnValue = self._current._rest.__len__()
      if response == 3:
        returnValue = self._current._rest.__contains__(value)
      if response == 4:
        returnValue = self._current._rest.__getitem__(index)
      if response == 5:
        returnValue = self._current._rest.count(value)
      if response == 6:
        returnValue = self._current._rest.index(value)
      if response == 7:
        returnValue = self._current._rest.append(value)
        
      if returnValue is not None:
        print(f'The function returned {returnValue}')
      else:
        print('The function completed (and did not return anything')
    except IndexError:
      print('The function raised an IndexError')
    except TypeError:
      print('The function raised an TypeError')
    except ValueError:
      print('The function raised an ValueError')
    except AttributeError:
      print('You cannot call a member function of self._rest, which is None')
    except:
      print('An exception was raised')

  def _setHead(self):
    validResponse = False
    while not validResponse:
      try:
        response = input('Enter a character: ').strip()
        if len(response) == 1 and response.isalpha():
          self._current._head = response
          validResponse = True
      except ValueError:
        pass
        
  def _newRest(self):
    self._current._rest = OurList()
    print('Done')
    
  def _getException(self):
    print('What type of exception should your raise?')
    print('  1)  TypeError')
    print('  2)  IndexError')
    print('  3)  ValueError')
    validResponse = False
    while not validResponse:
      try:
        response = int(input('What type of exception? '))
        if 1 <= response <= 3:
          validResponse = True
      except ValueError:
        print('Enter a number from 1 to 3')
    
    if response == 1:
      return 'TypeError'
    if response == 2:
      return 'IndexError'
    if response == 3:
      return 'ValueError'
  
class OurList:
  """Our own implementation of a python-style list."""

  def __init__(self):
    """Construct a new (empty) list."""
    self._head = None
    self._rest = None
  
  def _isEmpty(self):
    """Return True if self represents an empty list; False otherwise.
  
    This is a nonpublic utility method.
    """
    return self._rest is None
  
  def __len__(self):
    """Return the number of elements in the list."""
    if self._isEmpty():
      return 0
    else:
      return 1 + len(self._rest)  # recurse
  
  def count(self, value):
    """Return the number of occurrences of given value in the list."""
    if self._isEmpty():
      return 0
    else:
      subtotal = self._rest.count(value)      #|recursion#
      if self._head == value:           #|additional match#
        subtotal += 1
      return subtotal
  
  def __contains__(self, value):
    """Return True if the list contains the value; False otherwise."""
    if self._isEmpty():
      return False
    elif self._head == value:
      return True
    else:
      return value in self._rest  # recurse
  
  def index(self, value):
    """Return the leftmost index at which the value appears in the list.
  
    Throw a ValueError if value is not in the list.
    """
    if self._isEmpty():
      raise ValueError('OurList.index(x): x not in list')
    elif self._head == value:
      return 0
    else:      # look in remainder of the list
      return 1 + self._rest.index(value)
  
  def __getitem__(self, i):
    """Return the value at index i of the list.
  
    Note:  this implementation does not accept negative indices.
    """
    if self._isEmpty():
      raise IndexError('list index out of range')
    elif i == 0:
      return self._head
    else:
      return self._rest[i-1]   # recurse
        
  def __setitem__(self, i, value):
    """Equivalent to self[i] = value
  
    Note:  this implementation does not accept negative indices.
    """
    if self._isEmpty():
      raise IndexError('list assignment index out of range')
    elif i == 0:
      self._head = value
    else:
      self._rest[i-1] = value  # recurse
  
  def __repr__(self):
    """Return a string representation of the list."""
    if self._isEmpty():
      return '[]'
    elif self._rest._isEmpty():
      return '[' + repr(self._head) + ']'
    else:
      return '[' + repr(self._head) + ', ' + repr(self._rest)[1:]   # remove extra [
      
  def __eq__(self, other):
    if self.__len__() != len(other):
      return False
    for i in range(len(other)):
      if self.__getitem__(i) != other[i]:
        return False
    return True

  def append(self, value):
    """Add the given value to the end of the list."""
    if self._isEmpty():
      self._head = value    #|we now have one element#
      self._rest = OurList()  #|followed by new empty list#
    else:
      self._rest.append(value)  #|pass it on#
  
  def insert(self, index, value):
    """Insert value into list so that placed at given index."""
    if self._isEmpty():       #|inserting at end; similar to append#
      self._head = value
      self._rest = OurList()
    elif index == 0:        #|new element goes here!#
      shift = OurList()
      shift._head = self._head
      shift._rest = self._rest
      self._head = value
      self._rest = shift
    else:             #|insert recursively#
      self._rest.insert(index-1, value)
  
  def remove(self, value):
    """Remove the first occurrence of the value.
  
    Throw a ValueError if value is not in the list.
    """
    if self._isEmpty():
      raise ValueError('OurList.remove(x): x not in list')
    elif self._head == value:
      self._head = self._rest._head
      self._rest = self._rest._rest
    else:
      self._rest.remove(value)

  def min(self):
    if self._isEmpty():
      return None
    m = self._rest.min()
    if m is None:
      return self._head
    return min(m, self._head)


if __name__ == '__main__':
  sim = OurListSimulator()
  serial = randint(0,10)

  menu = (
    ('Experiment with _isEmpty', sim.isEmptyCase),
    ('Experiment with __len__', sim.lenCase),
    ('Experiment with __contains__', sim.containsCase),
    ('Experiment with __getitem__', sim.getItemCase),
    ('Experiment with count', sim.countCase),
    ('Experiment with index', sim.indexCase),
    ('Experiment with append', sim.appendCase),
    ('Quit',None),
    )

  done = False
  while not done:
    print()
    print('What would you like to do?')
    for k,option in enumerate(menu):
      print(f'{1+k:3})  {option[0]}')
    validResponse = False
    while not validResponse:
      try:
        response = int(input('Enter your choice: '))
        if 1 <= response <= len(menu):
          validResponse = True
      except ValueError:
        print(f'Enter a number from 1 to {len(menu)}')
        
    print()
    chosen = menu[response-1]
    if chosen[0] == 'Quit':
      done = True
      print('Goodbye')
    else:
      case = chosen[1](serial)   # use serial to force variety of scenarios
      serial += 1
      
    if not done:
      sim.run(case)
    print()
