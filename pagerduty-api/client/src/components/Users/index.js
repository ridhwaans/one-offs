import React, { useEffect, useState } from "react";
import { getUsers } from "../../api"

const Users = () => {
    const [inputFieldValue, setInputFieldValue] = useState("");
    const [users, setUsers] = useState([])
    const [flattenedUsers, setFlattenedUsers] = useState({
        headers: [],
        data: []
      });

      const fetchUsers = async () => {
        let users = await getUsers()
        
        return { users }
    }

      useEffect(() => {
        fetchUsers().then(response => {

            setUsers(response.users.data)
            const ourFlattenedUsers = flattenUsers(
                response.users.data.map(user => user)
              );
              setFlattenedUsers(ourFlattenedUsers);
        })

        return () => {
            setUsers(null)
        }
    }, [])

    const flattenUsers = (users) => {
        const data = [];
        for (const { id, name, email, contact_methods } of users) {
          data.push({
            id: id,
            name: name,
            email: email,
            contact_method_id: contact_methods[0].id,
            contact_method_type: contact_methods[0].type,
            contact_method_summary: contact_methods[0].summary,
            contact_method_self: contact_methods[0].self
          });
        }
      
        const headers = extractObjectKeys(data[0]);
        return { headers, data };
      };

      const extractObjectKeys = (object) => {
        let objectKeys = [];
      
        Object.keys(object).forEach((objectKey) => {
          const value = object[objectKey];
          if (typeof value !== "object") {
            objectKeys.push(objectKey);
          } else {
            objectKeys = [...objectKeys, ...extractObjectKeys(value)];
          }
        });
      
        return objectKeys;
      };

      const getFilteredRows = (rows, filterKey) => {
        return rows.filter((row) => {
          return Object.values(row).some((s) =>
            ("" + s).toLowerCase().includes(filterKey)
          );
        });
      };

    return (
      <React.Fragment>
          <input
            value={inputFieldValue}
            onChange={(e) => {
            setInputFieldValue(e.target.value);
            }}
          />
          <table>
              <thead>
              <tr>
                {flattenedUsers && flattenedUsers.headers.map(
                (userKey, userIdx) => (
                  <th
                  key={userIdx}
                  onClick={() => {
                      //sortColumn(userKey);
                  }}
                  >
                  {userKey}
                  </th>
                )
                )}
              </tr>
              </thead>
              <tbody>
              {getFilteredRows(flattenedUsers.data, inputFieldValue).map(
                (user, userIdx) => (
                <tr key={userIdx}>
                  {flattenedUsers.headers.map((header, headerIdx) => (
                  <td key={headerIdx}>{user[header]}</td>
                  ))}
                </tr>
                )
              )}
              </tbody>
          </table>
      </React.Fragment>
    );
  };
  
  export default Users;