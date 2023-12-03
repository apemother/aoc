mod input;

use regex::Regex;

fn find_first_last_single_digit(s: &str) -> Option<u8> {
    let re = Regex::new(r"\d").unwrap();
    let mut first_digit: Option<u8> = None;
    let mut last_digit: Option<u8> = None;

    for cap in re.captures_iter(s) {
        let digit: u8 = cap[0].parse().unwrap();
        if digit < 10 {
            if first_digit.is_none() {
                first_digit = Some(digit);
            }
            last_digit = Some(digit);
        }
    }

    if let (Some(first), Some(last)) = (first_digit, last_digit) {
        Some(first * 10 + last)
    } else {
        None
    }
}

fn solution_1() {
    let text = input::get_input1();
    let mut result: u32 = 0;
    for line in text.lines() {
        result += u32::from(find_first_last_single_digit(line).unwrap());
    }

    println!("{:?}", result);
}

fn main() -> std::io::Result<()> {
    println!("{:?}", solution_1());

    Ok(())
}
