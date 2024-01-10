import argparse

# Dictionary containing code snippets for different languages
code_snippets = {
    "python": {
        "hello_world": '''# Python code
print("Hello, World!")''',
        "ifelse": '''# Python code for if-else statement
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")''',
        "input": '''# Python code for input
name = input("Enter your name: ")
print("Hello,", name)'''
    },
    "rust": {
        "hello_world": '''// Rust code
fn main() {
    println!("Hello, World!");
}''',
        "ifelse": '''// Rust code for if-else statement
fn main() {
    let x = 5;
    if x > 10 {
        println!("x is greater than 10");
    } else {
        println!("x is less than or equal to 10");
    }
}''',
        "input": '''// Rust code for input (requires importing a crate)
use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter your name: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    println!("Hello, {}", input);
}'''
    },
    # ... other languages and snippets

    "haskell": {
        "hello_world": '''main :: IO ()
main = putStrLn "Hello, World!"''',
        "args_usage": '''import System.Environment

main :: IO ()
main = do
    args <- getArgs
    putStrLn ("Arguments: " ++ show args)'''
        # Haskell doesn't have direct terminal input similar to Python
    },
    "scala": {
        "hello_world": '''object HelloWorld {
    def main(args: Array[String]): Unit = {
        println("Hello, World!")
    }
}''',
        "args_usage": '''object ArgsUsage {
    def main(args: Array[String]): Unit = {
        println("Arguments: " + args.mkString(", "))
    }
}'''
        # Scala doesn't have direct terminal input similar to Python
    },
    # ... other languages and snippets

    "powershell": {
        "hello_world": '''Write-Output "Hello, World!"''',
        "args_usage": '''$args -join " "'''
        # PowerShell doesn't have direct terminal input similar to Python
    },
        "clojure": {
        "hello_world": '''(println "Hello, World!")''',
        "args_usage": '''(println (apply str "Arguments: " *command-line-args*))'''
        # Clojure doesn't have direct terminal input similar to Python
    },
    "groovy": {
        "hello_world": '''println "Hello, World!"''',
        # Groovy doesn't have if-else constructs in the same way as other languages
        # To keep it simple, here's just an output operation
    },
    "lua": {
        "hello_world": '''print("Hello, World!")''',
        # Lua doesn't have if-else constructs in the same way as other languages
        # To keep it simple, here's just an output operation
    },
    "matlab": {
        "hello_world": '''disp('Hello, World!')''',
        "args_usage": '''disp(['Arguments: ' strjoin(argv(), ' ')])'''
        # MATLAB doesn't have direct terminal input similar to Python
    }
}

def generate_code(language, operation, save=False):
    if language in code_snippets:
        if operation in code_snippets[language]:
            code = code_snippets[language][operation]
            if save:
                file_name = f"generated_{operation}.{language}"
                with open(file_name, "w") as file:
                    file.write(code)
                print(f"Generated {operation} in {language} has been saved to {file_name}")
            else:
                print(code)
        else:
            print(f"Sorry, operation '{operation}' not available for {language}.")
            if language in ["php", "haskell", "scala", "powershell"]:
                print(f"{language.capitalize()} doesn't have direct terminal input similar to Python.")
    else:
        print(f"Sorry, {language} language is not supported.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code snippets")
    parser.add_argument("language", help="Programming language to generate code for")
    parser.add_argument("operation", help="Operation to generate code for")
    parser.add_argument("--save", action="store_true", help="Save code to a file")

    args = parser.parse_args()
    generate_code(args.language.lower(), args.operation.lower(), args.save)
