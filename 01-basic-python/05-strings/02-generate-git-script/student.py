# Write your code here
def generate_git_script(id):
    updated_script = '''if [ ! -d id ]; then
    git clone https://github.com/id/project id
else
    (cd id; git pull)
fi'''.replace('id', id)

    return updated_script