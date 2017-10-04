# lazygit "My commit msg"
function lazygit() {
    git add .
    git commit -a -m "$1"
    git push
}

red=$(tput setaf 1)
green=$(tput setaf 2)
blue=$(tput setaf 4)
yellow=$(tput setaf 3)
reset=$(tput sgr0)
export PS1='\[$red\]\u\[$reset\]@\[$green\]\h\[$reset\]:\[$yellow\]\w\[$reset\]\$ '
