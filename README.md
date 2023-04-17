# EarthBound-Beginnings-ITA
Fan Italian translation of EarthBound Beginnings (MOTHER).

## ORIGINAL README
The text box contains max 22 characters in a line.<br>
Every overworld sentence begins with `*` and the following lines with a space ` `.<br>
Newlines are represented by the hash `#`.<br>
Pauses by `_`.<br>
The string ends where the characters `|` or `§` appear.<br>

**Example:**
```
*Hi, how are you# today?#_*Fine, hopefully!#|
```
**Result:**
![image](https://user-images.githubusercontent.com/131027007/232634204-facfef4d-b0ef-4e70-906e-5c63ae1fd3c3.png)

### SPECIAL COMBINATIONS
These combinations are read by the game as variables, then remember to treat them as if they were at their maximum length, written in brackets:<br />
` ¹÷[ ` => Ninten (7)<br />
` ¹£@ ` => Party Leader (7)<br />
` ¹x[ ` => Lloyd (7)<br />
` ¹8[ ` => Ana (7)<br />
` ¹¡] ` => Teddy (7)<br />
`` ¹|` `` => Complement (7)<br />
`` ¹°` `` => Subject (7)<br />
` ¹Ì× ` => Favorite Food (11)<br />
`` ¹%` `` => Item (11)<br />
`` ¹⁴` `` => Object (11)<br />
` ¹É& ` => Target (12)<br />
` ¹à& ` => Enemy (12)<br />
` ¹®& ` => ?? (11)<br />
` ¹°[ ` => Player Name (17)<br />
` ³ ` followed by 4 characters => Number (5)

### ITEMS/PSI/ENEMIES/LOCATIONS
All the lines in `items.txt` can't be longer than 11 characters, `|` doesn't count.

### BATTLE TEXT

The battle text uses different formatting rules: sometimes it's just plain text without `*`s and other times it is indented by one space at every line.
