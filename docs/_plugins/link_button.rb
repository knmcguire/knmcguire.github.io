require_relative 'plugin_helper'

module Jekyll
  class LinkButton < Liquid::Tag
    include Jekyll::PluginHelper

    def initialize(tag_name, text, tokens)
      super
      @params = parse_args(text)
    end

    def render(context)
        '<a href="' + @params[1] + '"><button name="button" style="background-color: #555555; border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        width: 100%; cursor: pointer"> '+@params[0] +'</button></a>'
    end
  end
end

Liquid::Template.register_tag('link_button', Jekyll::LinkButton)