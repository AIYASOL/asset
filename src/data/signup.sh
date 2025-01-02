#!/bin/bash

# Function to handle user input
get_input() {
  local prompt=$1
  local input
  read -p "$prompt: " input
  echo $input
}

# Check if username already exists (for simplicity, we assume a file storing users)
check_existing_user() {
  local username=$1
  if grep -q "^$username:" users.txt; then
    echo "Username already exists. Please choose another."
    return 1
  else
    return 0
  fi
}

# Sign-up process
sign_up() {
  echo "Welcome to AI Aiya - Sign Up!"

  # Get username
  while :; do
    username=$(get_input "Enter your username")
    check_existing_user $username
    if [ $? -eq 0 ]; then
      break
    fi
  done

  # Get email
  email=$(get_input "Enter your email")

  # Get password
  password=$(get_input "Enter your password")

  # Confirm password
  while :; do
    confirm_password=$(get_input "Confirm your password")
    if [ "$password" == "$confirm_password" ]; then
      break
    else
      echo "Passwords do not match. Please try again."
    fi
  done

  # Save user to the file (appending to 'users.txt')
  echo "$username:$email:$password" >> users.txt
  echo "Sign up successful! You can now log in."

}

# Check if users.txt exists, if not, creat
