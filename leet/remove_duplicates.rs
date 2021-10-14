pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    if nums.len() == 0 {
            return 0;
        } else {
            let mut prev_index: usize = 0;
            let mut index: usize = 1;

            while nums.len() > index {
                // println!("{:?},{}, {}", nums,index, prev_index);
                if nums[index] == nums[prev_index] {
                    nums.remove(index);
                } else {
                    prev_index = index;
                    index += 1;
                }
            }

            return index as i32;
    }
}

fn main() {
    let mut n = vec![1,1,2];

    println!("{}, {:?}", remove_duplicates(&mut n), n);
}