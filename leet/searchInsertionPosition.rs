pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
    let mid_index: usize = (nums.len() / 2) as usize;

    if nums.is_empty() {return 1;}

    if nums[mid_index] == target {
        return mid_index as i32;
    } else if nums.len() == 1 {
        return (nums[mid_index] < target) as i32;
    } else if nums[mid_index] > target {
        return search_insert(nums[..mid_index].to_vec(), target);
    } else {
        return mid_index as i32 + search_insert(nums[mid_index..].to_vec(), target);
    } 
}

fn main() {
    let t1:Vec<i32> = vec![1,3,5,6];
    println!("s: {}", search_insert(t1, 0));
}