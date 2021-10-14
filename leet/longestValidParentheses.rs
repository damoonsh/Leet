use std::collections::LinkedList;
/*
 * There first has to be an opening: [, (, {
 * Then given that there is a closing ] ) } it should match the last one added
 * Keep track of the longest one and restore given that there was an inconsistency
 */

 fn get_opposite(closing: char, opening: Option<char>) -> bool {
     // Checks to see if the opening and closing brackets match or not
     match closing {
         ']' => return opening == Some('['),
         ')' => return opening == Some('('),
         '{' => return opening == Some('{'),
         _ => false,
     }
} 

fn longest_valid_parentheses(s: String) -> i32 {
    let mut stack: LinkedList<char> = LinkedList::new();
    let mut longest: i32 = 0;
    let mut temp: i32 = 0;

    for elem in s.chars() {
        println!("{:?}, longest: {}, temp: {}", stack, longest, temp);
        // if there is an opening
        if (elem == '[') | (elem == '(') | (elem == '{') {
            if stack.is_empty() {temp = 0;}
            stack.push_front(elem);
        } else { // no opening
            let head = stack.pop_front();

            if get_opposite(elem, head) {
                temp += 2;
            } else {
                if temp > longest {longest = temp;} // see if there is a new longest
                temp = 0; // reset temporary
                stack.clear(); // reset the stack since the longest one is not the given sequence
            }
        }
    }

    if temp > longest { return temp; }

    longest
}

fn main() {
    let s: String = String::from("()(()");

    println!("{}", longest_valid_parentheses(s));
}