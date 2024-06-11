#!/bin/bash

# Check if npm is installed
if ! command -v npm &> /dev/null
then
    echo "npm could not be found. Please install Node.js and npm first."
    exit 1
fi

# Install Tailwind CSS as a development dependency
echo "Installing Tailwind CSS..."
npm install -D tailwindcss

# Initialize Tailwind CSS configuration
echo "Initializing Tailwind CSS configuration..."
npx tailwindcss init

echo "Tailwind CSS installation and initialization completed successfully."
