-- Create a trigger changing item quantity, i.e decreases
-- After adding a new order to items table

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
