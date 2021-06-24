fn length_of_longest_substring(s: String) -> i32 {
    let mut l: Vec<char> = Vec::new();
    let mut biggest_index: i32 = 0;

    for c in s.chars() {
        if l.iter().any(|&e| e == c) {
            
            if l.len() > biggest_index as usize { biggest_index = l.len() as i32; }

            let index = l.iter().position(|&r| r == c).unwrap();
            for i in 0..index{
                l.remove(0);
            }
        }
        l.push(c);
    }
    
    if l.len() as i32 > biggest_index { return l.len() as i32;}
    
    biggest_index
}

fn main() {
    let s = String::from("pwwkew");
    println!("{}", length_of_longest_substring(s));
}