import { Sidebar, SidebarContent, SidebarFooter, SidebarGroup, SidebarGroupContent, SidebarGroupLabel, SidebarMenu, SidebarMenuButton, SidebarMenuItem } from "@/components/ui/sidebar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@radix-ui/react-dropdown-menu";
import { ChevronUp, Upload, User2, ClipboardList } from "lucide-react";
import { Link } from "react-router-dom";


const items = [
  {
    title: "Subir Receta",
    url: "/dashboard/subir-receta",
    icon: Upload,
  },
  {
    title: "Recetas Publicadas",
    url: "/dashboard/recetas",
    icon: ClipboardList,
  },
]

export default function AppSidebar() {

  return (
    <Sidebar className="bg-sidebar-primary">
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel className="text-2xl mx-auto font-bold text-[#0A4486] m-5"
          >
            <Link to={'/'}>GastroMundo</Link>
          </SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <Link to={item.url} className="mt-5">
                      <item.icon size={30} className="font-bold"/>
                      <span className="text-[0.9rem] font-bold">{item.title}</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <SidebarMenu>
          <SidebarMenuItem>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <SidebarMenuButton>
                  <User2 /> Username
                  <ChevronUp className="ml-auto" />
                </SidebarMenuButton>
              </DropdownMenuTrigger>
              <DropdownMenuContent
                side="top"
                className="w-[--radix-popper-anchor-width]"
              >
                <DropdownMenuItem>
                  <span className="shadow px-6 py-2 cursor-pointer">Sign out</span>
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
    </Sidebar>
  )
}
