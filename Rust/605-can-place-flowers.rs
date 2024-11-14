impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, n: i32) -> bool {
        let len = flowerbed.len();
        let mut flowers = 0;
        let mut prev = 0;
        let mut next = 0;
        for i in 0..len {
            next = if i == len-1 {0} else {flowerbed[i+1]};
            if flowerbed[i] == 0 && prev == 0 && next == 0 {
                flowers += 1;
                flowerbed[i] = 1;
            }
            prev = flowerbed[i];
        }
        flowers >= n
    }
}

// Loop through
// If our current doesn't have a 1 on the right and doesn't have a 1 on the left, we can plant (set to 1)