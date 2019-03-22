
// Create an admin user.
use admin
db.createUser({
    user: "master",
    pwd: "eHzbJEmwi5GPNhDESr6KWu1wi",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ],
    passwordDigestor: "server"
})


// Using db tool to import and export collections.
// Run commands on bash.
{
	"repository": "https://bitbucket.org/rigsteam/tools-kit/src/master/",
	"example": {
		"import": "db --export -h production -d business -c user -f users.json",
		"export": "db --export -h production -d business -c order -f orders.json"
	}
}
