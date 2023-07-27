"use client";
import { useRouter } from 'next/navigation';
import { usePathname } from "next/navigation";
import { useMemo } from "react";
import Usermenuitem from './Usermenuitem';
const Usermenu = () => {
    const pathname = usePathname();
    const router = useRouter();
    const routes = useMemo(() => [
        {

            label: 'Home',
            active: pathname != '/',
            href: '/'
        },
        {

            label: 'About',
            active: pathname != '/About',
            href: '/About'
        },
        {

            label: 'Dashboard',
            active: pathname != '/Dasboard',
            href: '/Dashboard'
        },
        {

            label: 'Data',
            active: pathname != '/Data',
            href: '/Data'
        },
        {

            label: 'Contact',
            active: pathname != '/Contac',
            href: '/Contact'
        }
    ], [pathname]);
    return ( 
        <div className="relative">
            <div className="flex flex-row items-center gap-3">
                {routes.map((item) => (
                    <Usermenuitem
                        key={item.label}
                        {...item}
                    />
                ))}
            </div>
        </div>
     );
}
 
export default Usermenu;