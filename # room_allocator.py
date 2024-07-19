# room_allocator.py

def allocate_rooms(groups, hostels):
    allocations = []
    
    # Sort groups by size (largest first)
    sorted_groups = sorted(groups, key=lambda g: g['members'], reverse=True)
    
    for group in sorted_groups:
        group_id = group['id']
        members = group['members']
        gender = group['gender']
        
        # Find suitable rooms
        suitable_rooms = [room for room in hostels if room['gender'] == gender and room['capacity'] >= members]
        
        if suitable_rooms:
            # Allocate the group to the smallest suitable room
            room = min(suitable_rooms, key=lambda r: r['capacity'])
            allocations.append({
                'group_id': group_id,
                'hostel_name': room['hostel_name'],
                'room_number': room['room_number'],
                'members_allocated': members
            })
            
            # Update room capacity
            room['capacity'] -= members
        else:
            # Handle cases where a single room can't accommodate the entire group
            remaining_members = members
            while remaining_members > 0:
                available_rooms = [room for room in hostels if room['gender'] == gender and room['capacity'] > 0]
                if not available_rooms:
                    break
                
                room = max(available_rooms, key=lambda r: r['capacity'])
                allocated = min(remaining_members, room['capacity'])
                allocations.append({
                    'group_id': group_id,
                    'hostel_name': room['hostel_name'],
                    'room_number': room['room_number'],
                    'members_allocated': allocated
                })
                
                room['capacity'] -= allocated
                remaining_members -= allocated
    
    return allocations