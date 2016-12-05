import os
import sys
import json
import codecs
import traceback
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sublime
import sublime_plugin

s = sublime.load_settings("GithubMarkdown.sublime-settings")

class GithubMarkdownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the full path of current file
        file_path = self.view.file_name()
        if not file_path:
            show_error('please save the file first')
        # get the content
        file_text = self.view.substr(sublime.Region(0, self.view.size()))
        # request github api to render in markdown mode. see: <https://developer.github.com/v3/markdown/>
        sublime.status_message('GithubMarkdown: request github api...')
        url = "https://api.github.com/markdown"
        data = {
            "text": file_text,
            "mode": "gfm"
        }
        data = json.dumps(data).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        }
        token = s.get('token', '') # generate a token here <https://github.com/settings/tokens>
        if token:
            headers['Authorization'] = 'token %s' % token
        req = Request(url, data=data, headers=headers, method='POST')
        try:
            body = urlopen(req).read().decode('utf-8')
        except HTTPError:
            e = sys.exc_info()[1]
            traceback.print_exc()
            if e.code == 401:
                show_error('Github API auth failed. Please check your OAuth token.')
            else:
                show_error('Github API responded in an unfriendly way :/')
            return
        except:
            # e = sys.exc_info()[1]
            # print(e)
            traceback.print_exc()
            show_error('Something went wrong. Please check the error message in console')
            return
        # save the html file
        html = sublime.load_resource('Packages/GithubMarkdown/template.html')
        style = sublime.load_resource('Packages/GithubMarkdown/github-markdown.css')
        filename = os.path.splitext(os.path.basename(file_path))[0]
        html = html.replace('{{ TITLE }}', filename) # use the file name as title
        html = html.replace('{{ STYLE }}', style) # embeded the style. see: <https://github.com/sindresorhus/github-markdown-css>
        html = html.replace('{{ BODY }}', body)
        html_filename = os.path.splitext(file_path)[0] + '.html'
        with codecs.open(html_filename, 'w', 'utf-8') as html_file:
            html_file.write(html)
        sublime.status_message('GithubMarkdown: ' + html_filename + ' converted successfully')

def show_error(text):
    sublime.error_message('GithubMarkdown:\n%s' % text)