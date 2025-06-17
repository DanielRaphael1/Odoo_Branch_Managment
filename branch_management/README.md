# Branch Management Module for Odoo 18 Community

This module provides multi-branch support for Odoo Community Edition, allowing complete data isolation between different branches of your organization.
Feel free to use it, and leave a ⭐ if it was of use for you

## Features

- Branch management with dedicated managers
- Data isolation between branches
- Branch-specific views and filters
- Branch dashboard with key metrics
- Smart buttons for quick access to branch data
- Demo data included

## Installation

1. Copy the `branch_management` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the module from the Apps menu

## Usage

### Branch Management

1. Go to Branches > Branch Management > Branches
2. Create new branches with:
   - Branch Name
   - Branch Code
   - Branch Manager

### User Assignment

1. Assign users to branches through their user form
2. Users will only see data from their assigned branch
3. Branch managers have full access to their branch data

### Data Isolation

The module automatically:
- Filters all records by branch
- Assigns new records to the current user's branch
- Restricts access to branch-specific data

## Security

- Regular users can only see their branch's data
- Branch managers have full access to their branch
- System administrators can see all data

## Demo Data

The module includes demo data for:
- 4 branches (Jerusalem, Ashdod, Beersheba, Modiin)
- Branch managers for each location

## Dependencies

- base
- hr
- calendar
- crm

## License

LGPL-3 
