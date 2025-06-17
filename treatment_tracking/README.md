# Treatment Tracking Module for Odoo 18 Community

This module provides comprehensive tracking and management of treatments, linking them to sales orders and automating the invoicing process. It's designed for businesses that offer treatment-based services and need to track treatment sessions, manage prepaid credits, and automate billing.

## Features

- Treatment types management
- Automatic treatment tracking in calendar events
- Prepaid credit system with remaining treatments counter
- Automatic invoice generation upon treatment completion
- Integration with sales orders and products
- Hebrew language support
- Treatment completion tracking per customer
- Smart buttons for quick access to completed treatments

## Installation

1. Copy the `treatment_tracking` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the module from the Apps menu

## Usage

### Treatment Types Setup

1. Go to Treatment Management > Settings > Treatment Types
2. Create treatment types with:
   - Treatment Name
   - Description
   - Active Status

### Product Configuration

1. Go to Products
2. Edit a product to add:
   - Treatment Type
   - This links the product to a specific treatment type

### Sales Order Management

1. Create a sales order with treatment products
2. The system automatically:
   - Links treatment type to order lines
   - Tracks completed treatments
   - Shows remaining treatments
   - Manages prepaid credits

### Treatment Tracking

1. Create calendar events for treatments
2. Required fields:
   - Treatment Type
   - Customer
   - Date and Time
3. After treatment:
   - Click "Mark Treatment as Completed"
   - System automatically:
     - Updates treatment count
     - Creates invoice
     - Updates remaining treatments

### Customer View

1. Access customer form to see:
   - Completed treatments count
   - Quick access to treatment history
   - Treatment completion statistics

## Features in Detail

- **Treatment Types**: Flexible management of different treatment types
- **Automatic Invoicing**: Generates invoices upon treatment completion
- **Credit Management**: Tracks remaining treatments from sales orders
- **Calendar Integration**: Links treatments to calendar events
- **Customer Tracking**: Monitors treatment history per customer
- **Hebrew Support**: Full Hebrew language interface

## Security

- Regular users can only see their own treatments
- Sales managers can see all treatments
- Treatment completion restricted to authorized users

## Dependencies

- base
- sale
- calendar
- account

## License

LGPL-3 