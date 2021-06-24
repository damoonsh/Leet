use std::collections::LinkedList;

fn identify_opening( c: char) -> bool {
    (c == '[') | (c == '{') | (c == '(')
}

fn solve(s: String) -> bool {
    
    let mut stack: LinkedList<char> = LinkedList::new();

    for l in s.chars() {
        if identify_opening(l) {
            stack.push_front(l);
        } else {
            let m = stack.pop_front();
            match l {
                ']' => if m != Some('[') { return false; },
                ')' => if m != Some('(') { return false; },
                '}' => if m != Some('{') { return false; },
                _ => (),
            }
        }
    }
    
    stack.is_empty()
}

fn main() {
    let s: String = "((()))".to_string();
    
    println!("s: {}", solve(s));
}
