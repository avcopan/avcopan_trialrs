// The crate docs are included from CRATE.md, which is also the crates.io page.
#![doc = include_str!("../CRATE.md")]

mod greet;

pub use greet::greet;

// The Python bindings are only compiled when the `python` feature is enabled.
#[cfg(feature = "python")]
mod python;
