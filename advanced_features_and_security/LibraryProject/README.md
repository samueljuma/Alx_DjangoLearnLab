
## Django Book Permissions System

### Features
- Enforces **role-based access** with **Groups & Permissions**.
- Uses `@permission_required` to restrict access.
- Supports **Viewers, Editors, and Admins** roles.


✅ **Step 1:** Defined **custom permissions** (`can_view`, `can_create`, `can_edit`, `can_delete`).  
✅ **Step 2:** Created **Viewers, Editors, Admins** groups and assigned permissions.  
✅ **Step 3:** Enforced **permissions in views** using `@permission_required`.  
✅ **Step 4:** **Tested** access for different users.  

