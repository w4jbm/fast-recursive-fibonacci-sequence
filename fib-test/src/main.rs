// fib-test.rs - Fibonacci Numbers Test Program in Rust
//
// This is a simple recursive program that originally demonstrated
// the @cache decorator in Python. Here it is using the #[memoize]
// attribute for Rust.
//
// This is my first use of Rust and cargo, so there is no elegance
// in the solution.
//
// .../fib-test$ cargo build
// .../fib-test$ cargo run
// 

use memoize::memoize;

#[memoize]
fn fib(n: u64) -> u64 {
    match n {
        0 => 1,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2),
    }
}

fn main() {
    let mut i = 0;
    while i < 46 {
        println!("{} {}",i, fib(i));
        i += 1;
    }
}
