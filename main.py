def define_env(env):
    @env.macro
    def skill_label(skill):
        """Generate a clickable skill label linking to the current page with a search query."""
        from urllib.parse import quote_plus
        skill_slug = quote_plus(skill)  # URL-safe skill name
        return f'<a href="?q={skill_slug}" class="skill-label">{skill}</a>'