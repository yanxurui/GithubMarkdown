# Github markdown converter plugin for sublime text 3
## preview
This is a sublime text 3 plugin for demo. It can render a markdown document like github README.md by calling github markdown api.

## installation
<!-- 
### Via Package Control
The easiest way is to install it via [Package Control](https://packagecontrol.io/).
* Go to **Command Palette** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> or <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
* Select **Package Control : Install Package**
* Search for **GithubMarkdown**
 -->
### Manual
* Clone the repository or download the ZIP
* Extract the archive
* Put it in your **Packages**( `Preferences > Browse Packages...` ) directory.

## settings
By setting the [OAuth token](https://github.com/settings/tokens), you can make up to 5,000 requests per hour. Otherwise, the rate limit allows you to make up to 60 requests per hour.

## key bindings
`ctrl+alt+g`

## todo
- [ ] not tested on linux(especially ssl problem)
- [x] main thread blocked
- [ ] animation on status bar while making request
- [x] tasks list not supported
- [x] context menu
- [ ] default settings is modifiable

### some knows issues
* `urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>`

## license
[MIT](https://opensource.org/licenses/MIT)